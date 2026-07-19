pipeline {
    agent any

    environment {
        IMAGE_NAME = "sigh1234/ai-performance-platform:1.0"
        KUBECONFIG = "C:\\Users\\LENOVO\\.kube\\config"
    }

    options {
        timestamps()
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Verify Workspace') {
            steps {
                bat '''
                echo ================================
                echo WORKSPACE
                echo ================================
                cd
                dir
                echo.
                dir docker
                echo.
                dir kubernetes
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                docker build -t %IMAGE_NAME% -f docker\\Dockerfile .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat '''
                docker push %IMAGE_NAME%
                '''
            }
        }

        stage('Verify Kubernetes') {
            steps {
                bat '''
                kubectl version
                kubectl config current-context
                kubectl get nodes
                '''
            }
        }

        stage('Delete Previous Job') {
            steps {
                bat '''
                kubectl delete job ai-performance-job --ignore-not-found=true
                '''
            }
        }

        stage('Deploy Kubernetes Job') {
            steps {
                bat '''
                kubectl apply -f kubernetes\\job.yaml
                '''
            }
        }

        stage('Wait For Completion') {
            steps {
                bat '''
                kubectl wait --for=condition=complete job/ai-performance-job --timeout=300s
                '''
            }
        }

        stage('Job Logs') {
            steps {
                bat '''
                kubectl logs job/ai-performance-job
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/**/*', fingerprint: true
            }
        }
    }

    post {

        always {
            echo "Pipeline Finished"
        }

        success {
            echo "SUCCESS: AI Performance Platform executed successfully."
        }

        failure {
            echo "FAILURE: Please check the stage where the pipeline stopped."
        }

        cleanup {
            bat 'docker image prune -f'
        }
    }
}