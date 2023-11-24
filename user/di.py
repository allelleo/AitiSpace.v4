from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.oci.governance import Groups
from diagrams.onprem.database import MySQL
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import RabbitMQ
from diagrams.programming.framework import FastAPI, React
from diagrams.saas.chat import Telegram

with Diagram('AitiSpace user service'):
    user = Groups('Our users')

    nginx = Nginx('nginx')
    load_balancer = ELB('Load Balancer')

    front = React('FrontEnd')
    with Cluster('backend'):
        backend = [
            FastAPI('backend1'),
            FastAPI('backend2'),
            FastAPI('backend3'),
        ]
    user >> front >> nginx >> load_balancer >> backend
    rabbit = RabbitMQ("Async Queue")
    backend >> rabbit
    backend >> Telegram("Alerts")
    with Cluster('Databases'):
        db = [
            MySQL('db1'),
            MySQL('db2'),
            MySQL('db3'),
        ]
    backend >> ELB("Database Load Balancer") >> db
    with Cluster('Workers'):
        wk = [
            EC2('worker1'),
            EC2('worker2'),
            EC2('worker3'),
            EC2('worker4'),
            EC2('worker5'),
        ]

    rabbit >> wk
