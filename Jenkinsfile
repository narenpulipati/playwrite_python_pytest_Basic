pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        PYTHON = "C:\\Users\\taccuser\\AppData\\Local\\Python\\bin\\python.exe"
        VENV_DIR = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                bat """
                    "%PYTHON%" --version
                    "%PYTHON%" -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    playwright install
                """
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    pytest -v ^
                        --junitxml=report.xml ^
                        --html=report.html ^
                        --self-contained-html
                """
            }
        }
    }

    post {
        always {

            junit 'report.xml'

            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Playwright HTML Report'
            ])
        }
    }
}