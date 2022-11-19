pipeline {
    agent any
    tools {
        nodejs '18.12.1'
    }
    stages {
        stage('build') {
            steps {
                sh 'python create_artifacts.py'
            }
        }
        stage('publish') {
              steps {
                  archiveArtifacts artifacts: 'build/'
              }
        }
    }
}
