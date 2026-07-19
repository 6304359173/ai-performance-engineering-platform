pipeline {
    agent any

    stages {

        

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t sigh1234/ai-performance-platform:1.0 -f docker/Dockerfile .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push sigh1234/ai-performance-platform:1.0'
            }
        }

        stage('Deploy Kubernetes Job') {
            steps {
                bat 'kubectl apply -f kubernetes/job.yaml'
            }
        }

        stage('Wait for Job') {
            steps {
                bat 'kubectl wait --for=condition=complete job/ai-performance-job --timeout=300s'
            }
        }

        stage('Job Logs') {
            steps {
                bat 'kubectl logs job/ai-performance-job'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
    }
}