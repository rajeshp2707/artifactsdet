pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 create_artifacts.py'
            }
        }
        stage('publish') {
              steps {
                  archiveArtifacts artifacts: '*.txt'
              }
        }
    }
}
