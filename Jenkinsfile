pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                // Create venv and install requirements
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                echo 'Running Unit Tests...'
                // Activate venv and run pytest
                bat 'venv\\Scripts\\activate.bat && pytest'
            }
        }
        
        stage('Build Application') {
            steps {
                echo 'Packaging application...'
                // Create a build directory and copy relevant files there
                bat 'if not exist dist mkdir dist'
                bat 'copy app.py dist\\'
                bat 'copy requirements.txt dist\\'
            }
        }
        
        stage('Deploy Application') {
            steps {
                echo 'Deploying application...'
                // Simulate deployment by copying to a temp folder on C drive
                bat 'if not exist C:\\Temp\\FlaskDeploy mkdir C:\\Temp\\FlaskDeploy'
                bat 'xcopy dist\\*.* C:\\Temp\\FlaskDeploy /Y /S'
            }
        }
    }
}