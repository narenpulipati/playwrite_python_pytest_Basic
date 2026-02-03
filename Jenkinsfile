pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/narenpulipati/playwrite_python_pytest.git'
            }
        }

        stage('Setup Python venv') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest with Report') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest --junitxml=reports\\results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/results.xml'
        }
        success {
            echo '✅ Tests passed'
        }
        failure {
            echo '❌ Tests failed'
        }
    }
}
