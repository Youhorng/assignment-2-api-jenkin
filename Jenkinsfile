pipeline {
    agent any

    environment {
        VENV_DIR = '/var/lib/jenkins/venv'
        REQ_HASH_FILE = '/var/lib/jenkins/.req_hash'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Youhorng/assignment-2-api-jenkin.git'
            }
        }

        stage('Setup Virtualenv & Install Dependencies') {
            steps {
                sh '''
                    # Create venv if it doesn't exist
                    # NOTE: python3.12-venv must be installed on the server manually:
                    #   sudo apt-get install -y python3.12-venv
                    if [ ! -d "$VENV_DIR" ]; then
                        python3 -m venv $VENV_DIR
                        echo "Virtual environment created."
                    fi

                    # Compute current requirements.txt hash
                    CURRENT_HASH=$(md5sum requirements.txt | awk '{ print $1 }')

                    # Read previously stored hash (if any)
                    PREV_HASH=""
                    if [ -f "$REQ_HASH_FILE" ]; then
                        PREV_HASH=$(cat $REQ_HASH_FILE)
                    fi

                    # Only install if requirements.txt changed
                    if [ "$CURRENT_HASH" != "$PREV_HASH" ]; then
                        echo "requirements.txt changed — installing dependencies..."
                        $VENV_DIR/bin/pip install -r requirements.txt
                        echo "$CURRENT_HASH" > $REQ_HASH_FILE
                    else
                        echo "requirements.txt unchanged — skipping install."
                    fi
                '''
            }
        }

        stage('Stop Old Server') {
            steps {
                sh '''
                    pkill -f "uvicorn main:app" || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    nohup $VENV_DIR/bin/uvicorn main:app --host 0.0.0.0 --port 8000 \
                        > /var/lib/jenkins/app.log 2>&1 &
                    echo "FastAPI deployed!"
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}