pipeline{
    environment {
        dockerimagename = "matiasolivar/py-app"
        dockerImage = ""
    }
    agent any
       
    stages{
        stage ("checkout SCM"){
            steps{
                git 'https://github.com/matix10/clase36-desafios.git'
            }

        }
       stage ("deploy to kubernetes"){
            steps{
                scipts {
                    kubernetesDeploy(configs:"Desafio2/deployment.yaml","Desafio2/pv.yaml","Desafio2/pvc.yaml","Desafio2/svc.yaml")
                }
            }
       }
        
}
}

