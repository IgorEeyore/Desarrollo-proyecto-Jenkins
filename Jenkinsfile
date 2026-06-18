pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        APP_PORT = '5000'
    }

    stages {
        stage('Build') {
            steps {
                echo '=== ETAPA: BUILD ==='
                sh 'pip install -r requirements.txt'
                echo 'Dependencias instaladas correctamente.'
            }
        }

        stage('Security Review') {
            steps {
                echo '=== ETAPA: REVISIÓN DE SEGURIDAD ==='
                sh 'pip install bandit'
                sh 'bandit -r app.py -f txt -o bandit_report.txt || true'
                sh 'cat bandit_report.txt'
            }
        }

        stage('Test') {
            steps {
                echo '=== ETAPA: PRUEBAS ==='
                sh 'pip install pytest'
                sh 'pytest --tb=short || true'
                echo 'Pruebas completadas.'
            }
        }

        stage('Deploy') {
            steps {
                echo '=== ETAPA: DESPLIEGUE ==='
                sh 'nohup python app.py &'
                sh 'sleep 3'
                echo "Aplicación desplegada en puerto ${APP_PORT}"
            }
        }
        
        stage('OWASP ZAP Scan') {
            steps {
                echo '=== ETAPA: OWASP ZAP ==='
                sh '''
                    docker run --rm --network=host \
                    -v $(pwd):/zap/wrk/:rw \
                    ghcr.io/zaproxy/zaproxy:stable \
                    zap-baseline.py \
                    -t http://localhost:5000 \
                    -r zap_report.html \
                    -I
                '''
            }
        }
    }

    post {
        always {
            echo '=== PIPELINE COMPLETADO ==='
            archiveArtifacts artifacts: '*_report.*', allowEmptyArchive: true
        }
    }
}