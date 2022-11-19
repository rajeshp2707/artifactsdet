pipeline {
    agent any
    tools {
        nodejs '18.12.1'
    }
    stages {
        stage('build') {
            steps {
                sh 'python3 create_artifacts.py'
            }
        }
        stage('publish') {
              steps {
                  archiveArtifacts artifacts: '**'
              }
        }
    }
}
