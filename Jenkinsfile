library identifier: "pipeline-library@v1.1",
retriever: modernSCM(
  [
    $class: "GitSCMSource",
    remote: "https://github.com/redhat-cop/pipeline-library.git"
  ]
)
library identifier: "brandi-pipeline-library@v1.2.4",
retriever: modernSCM(
  [
    $class: "GitSCMSource",
    remote: "ssh://git@gitlab.agilesof.com/brandi-dev/pipeline-library.git",
    credentialsId: 'brandi-ci-cd-ssh-private-key'
  ]
)

openshift.withCluster() {

  env.NAMESPACE = openshift.project()
  env.APP_NAME = "brandi-candidate-service"
  env.APP_VERSION = "0.0.1"
  env.BUILD = "${env.NAMESPACE}"
  env.DEV = env.BUILD.replace('ci-cd', 'dev')
  env.TEST = env.BUILD.replace('ci-cd', 'test')
  env.BASE_IMAGE = "brandi-python-ubi:v0.0.2"

  env.BUILD_OUTPUT_DIR = env.PIPELINE_CONTEXT_DIR ? "${env.PIPELINE_CONTEXT_DIR}" : "."

  echo "Starting Pipeline for ${APP_NAME}..."

}

pipeline {
  // Use Jenkins Python slave
  // Jenkins will dynamically provision this as OpenShift Pod
  // All the stages and steps of this Pipeline will be executed on this Pod
  // After Pipeline completes the Pod is killed so every run will have clean
  // workspace
  agent {
    label 'jenkins-slave-python'
  }

  environment {
    PIPENV_VENV_IN_PROJECT = "true"
  }
  // Pipeline Stages start here
  // Requeres at least one stage
  stages {

    // Setup Python with PIPENV and create VENV
    stage('Setup Environment') {

        steps {

          script {
            env.APP_HASH = env.APP_VERSION + "-" + sh (script: "git log -n 1 --pretty=format:'%H'", returnStdout: true)
            sh """
               set -e
               pip install --user pipenv
               cd ${env.BUILD_OUTPUT_DIR}
               pipenv sync
               pipenv install --dev
               """
          }

        }

    }

    // Run Dependency Check
    stage('Dependency Check') {
        steps {
            sh "pipenv check"
            // TODO:  Need to validate success
        }
    }

    stage('Run Tests') {

      steps {
        sh """
           set -e
           source .venv/bin/activate
           pytest tests --junitxml=report.xml
           deactivate
           """
      }

      post {
        always {
          junit '**/report.xml'
        }
      }

    }

    stage('Build & Deploy runtime-image to DEV'){
      steps {
        script {
          def dockerfile_content = readFile("${env.WORKSPACE}/Dockerfile")

          ubiBinaryBuild(fromImage: env.BASE_IMAGE, buildOutputDir: env.BUILD_OUTPUT_DIR, devNamespace: env.DEV, appName: env.APP_NAME, appTag: env.APP_HASH, dockerfileContent: dockerfile_content)
          updateDeployment(devNamespace: env.DEV, appName: env.APP_NAME, appTag: env.APP_HASH)
        }
      }
    }

    stage ('Tag recently built image as Latest') {
      steps {
        tagImage(sourceImageName: env.APP_NAME , sourceImageTag: env.APP_HASH, sourceImagePath: env.DEV, toImageName: env.APP_NAME , toImageTag: "latest", toImagePath: env.DEV)
      }
    }

    stage ('Verify Deployment to Dev') {
      steps {
        verifyDeployment(projectName: env.DEV, targetApp: env.APP_NAME)
      }
    }

    stage('Promotion gate') {
      steps {
        script {
          timeout(time: 15, unit: 'MINUTES') {
            input message: 'Promote application to Test?'
          }
          milestone 1 // if newer build runs and gets past this point, all previous builds still running will die
        }
      }
    }

    stage('Promote from Dev to Test') {
      steps {
        tagImage(sourceImageName: env.APP_NAME, sourceImagePath: env.DEV, toImagePath: env.TEST)
      }
    }

    stage ('Verify Deployment to Test') {
      steps {
        verifyDeployment(projectName: env.TEST, targetApp: env.APP_NAME)
      }
    }


  }
}

