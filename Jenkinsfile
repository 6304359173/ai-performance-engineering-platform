pipeline {
    agent any

    stages {
        stage('Show Workspace') {
    steps {
        bat 'dir'
        bat 'dir docker'
    }
}
     stage('Verify Workspace') {
    steps {
        bat 'echo Current Directory'
        bat 'cd'
        bat 'dir'
        bat 'dir docker'
    }
}   

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t sigh1234/ai-performance-platform:1.0 -f docker/Dockerfile .'
            }
        }

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

stage('Verify Kubernetes') {
    steps {
        bat '''
        set KUBECONFIG=%USERPROFILE%\\.kube\\config
        kubectl version
        kubectl config current-context
        kubectl get nodes
        '''
    }
}

stage('Deploy Kubernetes Job') {
    steps {
        bat '''
        set KUBECONFIG=%USERPROFILE%\\.kube\\config
        kubectl delete job ai-performance-job --ignore-not-found=true
        kubectl apply -f kubernetes\\job.yaml
        '''
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