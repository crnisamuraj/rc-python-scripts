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

def main():
	URL = "https://chat.doobinnovation.com/hooks/eZfAC2BgpD6vPLwS8/r9GKi89vNMJiJwh4p5PewfviPkg5pEzThNjWzBxnivJCReds"
	scanPath = "TestScanPath"
	scanId = "Scan ID"
	feedback = "Some feedback goes here. Explain what needs to be fixed etc"
	color = "#764FF5"

	parser = argparse.ArgumentParser(description='Script for ez posting to rocket.Chat webhook for QC fails')
	parser.add_argument("-sp", "--scan-path", dest="scanPath", help="Full path to scan")
	parser.add_argument("-id", "--scan-id", dest="scanId", help="Scan id")
	parser.add_argument("-f", "--feedback", dest="feedback", help="Feedback message")
	parser.add_argument("-c", "--color", dest="color", help="message color", default=color)
	parser.add_argument("-u", "--url", dest="url", help="message color", default=URL)
	
	args = parser.parse_args()

	URL=args.url
	scanPath = args.scanPath
	scanId = args.scanId
	feedback = args.feedback
	color = args.color

	message = Message(args.scanPath, args.scanId, args.feedback, args.color)

	r = requests.post(url = URL, data = message.craftMessage())

if __name__ == "__main__":
	main()
