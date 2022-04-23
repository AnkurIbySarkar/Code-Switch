from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer, AutoModelForSequenceClassification

class LanguageIdentification(object):
        elif self.language == "hin-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-hineng-lid-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-hineng-lid-lince")
            print("Model Download Completed!")
    def identify(self, text):
        lid_model = pipeline('ner', model=self.model, tokenizer=self.tokenizer)
        results = lid_model(text)
        return results
