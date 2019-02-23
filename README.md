# answerForDiafaan
Make http requests and send the answers to your diafaan. # Http integration


Config.json file structure

{
  "database" : {
    "host" : "your_host",
    "user" : "diafaan",
    "passwd" : "501jN1IApyAYakix",
    "database" : "server_diafaan"
  },
  "request":{
    "url": "http://208.115.208.17/?p=/api/resposta",
    "method" : "POST",
    "param" : {
      "key" : "your_key"
    }
  },
  "payloadName" : "content",
  "successString" : "\"status\":\"sucesso\"",
  "expectedResponseParameters":{
    "sendTime" : "hora",
    "formatDate" : "%d/%m/%Y %H:%M:%S",
    "from" : "remetente",
    "to" : "",
    "text" : "mensagem"
  },
  "databaseTableTarget" : "Servidor_entrada"
}
