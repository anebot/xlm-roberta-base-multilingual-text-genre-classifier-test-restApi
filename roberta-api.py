from flask import Flask, request, jsonify
from simpletransformers.classification import ClassificationModel

app = Flask(__name__)

model_args= {
            "num_train_epochs": 15,
            "learning_rate": 1e-5,
            "max_seq_length": 512,
            "silent": True
            }
            
model = ClassificationModel(
    "xlmroberta", "classla/xlm-roberta-base-multilingual-text-genre-classifier", use_cuda=False,
    args=model_args)

### Example of run:
### curl -X POST -H "Content-Type: application/json" -d '{"input_string": ["On our site, you can find a great genre identification model which you can use for thousands of different tasks."]}' http://127.0.0.1/api/classify
@app.route('/api/classify', methods=['POST'])
def echo():
    try:
        data = request.get_json()  # Assuming the input is in JSON format
        if 'input_string' in data:
            input_string = data['input_string']
            
            print(input_string)
            # Perform any processing if needed
            
            predictions, logit_output = model.predict(input_string)
            
            lstpred = logit_output.tolist();
            ##result = f"You sent: {input_string}"
            return jsonify(result=lstpred)
        else:
            return jsonify(error='Parameter "input_string" is missing'), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/tags', methods=['GET'])
def showTags():
    return jsonify({0: 'Other', 1:'Information/Explanation',2: 'News',3: 'Instruction',4: 'Opinion/Argumentation',5: 'Forum',6: 'Prose/Lyrical',7: 'Legal',8: 'Promotion'})

if __name__ == '__main__':
    app.run(debug=True)

