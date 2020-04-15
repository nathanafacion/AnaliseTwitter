from twitter import Twitter
from db import Database
from datetime import datetime , timedelta
from emotion import EmotionTwitter
from graph import Graph
from generatePDF import GeneratePDF
import argparse
import createlog

def main():

    parser = argparse.ArgumentParser(description='Lista de parametros a ser utilizado:')
    parser.add_argument('--origin', metavar='N', type=str,
                    help='Linguagem atual do texto (default:pt)', default='pt')
    parser.add_argument('--action', help='Se quiser inserir digite (1), se quiser gerar relatorio digite (2) (default:1)', default=2)
    parser.add_argument('--tag', help='Qual a palavra que deseja ver as emotion (Default:Nintendo)',default='Nintendo')
    parser.print_help()

    args = parser.parse_args() 

    if args.action == 1:
        createlog.logger.info('Action 1')

           
        twitters = ['Eu amo o Joao. Te amo','Rato eh azul']
        
        for text in twitters:
            em = EmotionTwitter(text,args.origin)
            em.sentences()
            listtwitter = []
            twitter = Twitter( datetime.now().strftime("%d/%m/%Y"), args.tag, em.polarity, em.objective)
            createlog.logger.info('Insert twitter - date:' + twitter.date + " tag:" + twitter.tag + " emotion:" +twitter.emotion + "Objetive: "+twitter.isObjective) 
            listtwitter.append(twitter)

        db = Database("db_twitter_emotion") 
        #db.removeAll()
        db.insertList(listtwitter)


        
        #for i in db.findAll():
    	#    logging.info(i)
    
    if args.action == 2:
     
        createlog.logger.debug('Action 2')
        
        date_init = datetime.now() - timedelta(days=7)
        date_init = date_init.strftime("%d/%m/%Y")
        date_end = datetime.now().strftime("%d/%m/%Y")

        createlog.logger.debug('Generate report - date:' + date_end) 
        
        # Criacao dos graficos
        x_neutro = [1,2,3,4,5,6,8] 
        x_positive = [0,6,7,8,9,10,9] 
        x_negative = [0,2,3,4,7,10,1] 
        y = [1,2,3,4,5,6,7]  
        
        createlog.logger.debug('Generate report - x_neutro:')
        createlog.logger.debug(x_neutro) 
        createlog.logger.debug('Generate report - x_positive:')
        createlog.logger.debug(x_positive) 
        createlog.logger.debug('Generate report - x_negative:')
        createlog.logger.debug(x_negative) 


        g_polarity = Graph('Dias', 'Quantidade  de twitter', 'Neutro x Positive x Negative', 'g_polarity.png')
        g_polarity.plot_graph( x_neutro,y, 'yellow', 'black', 'Neutro')
        g_polarity.plot_graph( x_negative,y, 'red', 'black', 'Negative')
        g_polarity.plot_graph( x_positive,y, 'green', 'black','Positive', True) 


        x_objetive = [0,6,7,8,9,10,2] 
        x_subjetive = [0,2,3,4,7,10,4]    

        createlog.logger.debug('Generate report - x_objetive:')
        createlog.logger.debug(x_objetive) 
        createlog.logger.debug('Generate report - x_subjetive:') 
        createlog.logger.debug(x_subjetive) 
        
        g_objetive = Graph('Dias', 'Quantidade  de twitter', 'Subjetivo x Objetivo', 'g_objetive.png')
        g_objetive.plot_graph( x_objetive,y, 'red', 'black','Objetive')
        g_objetive.plot_graph( x_subjetive,y, 'green', 'black', 'Subjetive' ,True)  

        # Relatorio a ser gerado  
        elements = [
		  { 'name': 'company_logo', 'type': 'I', 'x1': 25.0, 'y1': 25.0, 'x2': 78.0, 'y2': 45.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'L', 'text': 'logo', 'priority': 2, },
		  { 'name': 'report_name', 'type': 'T', 'x1': 100.0, 'y1': 30.0, 'x2': 180.0, 'y2': 37.5, 'font': 'Arial', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
		  { 'name': 'report_tag', 'type': 'T', 'x1': 125.0, 'y1': 30.0, 'x2': 180.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
		  { 'name': 'text_info', 'type': 'T', 'x1': 25.0, 'y1': 50.0, 'x2': 180.0, 'y2': 70.0, 'font': 'Arial', 'size': 8.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
		  { 'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 0, },
		  { 'name': 'line1', 'type': 'L', 'x1': 25.0, 'y1': 50.0, 'x2': 180.0, 'y2': 50.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
		  { 'name': 'line2', 'type': 'L', 'x1': 90.0, 'y1': 17.0, 'x2': 90.0, 'y2': 50.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
		  { 'name': 'graph1', 'type': 'I', 'x1': 20.0, 'y1': 70.0, 'x2': 150, 'y2': 150.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'L', 'text': 'logo', 'priority': 2, },
		  { 'name': 'graph2', 'type': 'I', 'x1': 20.0, 'y1': 150.0, 'x2': 150, 'y2': 230.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'L', 'text': 'logo', 'priority': 2, },
		]
	g = GeneratePDF(elements)
	g.addtext('report_name', "Report about:")
	g.addtext("report_tag", args.tag)
	g.addtext("text_info", "Analise de Objetividade e de Sentimentos do twitter do dia "+ date_init + " ao dia " + date_end + ".")
	g.addimage("company_logo","report.png")
	g.addimage("graph1",g_polarity.figurename)
	g.addimage("graph2",g_objetive.figurename)
	g.generatePDF("relatorio.pdf")

	createlog.logger.debug('Generate pdf') 

 
if __name__ == "__main__":
    main()

  # como rodar o arquivo de forma agendada no pc https://e-tinet.com/linux/crontab/
  # log  https://docs.python.org/3/howto/logging.html#logging-basic-tutorial como colocar log em outro arquivo?
