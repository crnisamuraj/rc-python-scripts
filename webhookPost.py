import requests
import json
import argparse

class Message:
	def __init__(self, scanPath, scanId, feedback, color):
		self.scanPath = scanPath
		self.scanId = scanId
		self.feedback = feedback
		self.color = color
	
	def craftMessage(self):
		messageBody = {
			"text":self.scanPath,
			"attachments":
			[{
				"title":self.scanId, 
				"text":self.feedback, 
				"color":self.color
			}]
		}
		return json.dumps(messageBody)

def post(URL, scanPath, scanId, feedback, color):
	message = Message(scanPath, scanId, feedback, color)
	r = requests.post(url = URL, data = message.craftMessage())

def main():
	URL = "https://chat.doobinnovation.com/hooks/eZfAC2BgpD6vPLwS8/r9GKi89vNMJiJwh4p5PewfviPkg5pEzThNjWzBxnivJCReds"
	scanPath = "Scan Path"
	scanId = "Scan ID"
	feedback = "Message"
	color = "#764FF5"

	parser = argparse.ArgumentParser(description='Script for ez posting to rocket.Chat webhook for QC fails')
	parser.add_argument("-sp", "--scan-path", dest="scanPath", help="Full path to scan", default=scanPath)
	parser.add_argument("-id", "--scan-id", dest="scanId", help="Scan id", default=scanId)
	parser.add_argument("-f", "--feedback", dest="feedback", help="Feedback message", default=feedback)
	parser.add_argument("-c", "--color", dest="color", help="message color", default=color)
	parser.add_argument("-u", "--url", dest="url", help="message color", default=URL)
	
	args = parser.parse_args()

	message = Message(args.scanPath, args.scanId, args.feedback, args.color)

	r = requests.post(url = URL, data = message.craftMessage())

if __name__ == "__main__":
	main()
