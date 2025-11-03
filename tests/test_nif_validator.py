        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-id',
                    passwordVariable: 'passwd', 
                    usernameVariable: 'username')]) {
                    sshagent(credentials: ['cluster-crendentials']) {
                        sh"""
                        ssh -o StrictHostKeyChecking=no redhat@172.31.33.7 docker rm -f ${JOB_BASE_NAME} || true
                        ssh -o StrictHostKeyChecking=no redhat@172.31.33.7 docker run -d --name ${JOB_BASE_NAME} -p 8080:9046 --pull always ${username}/${JOB_BASE_NAME}
                        """
                    }
                }
            }
        }