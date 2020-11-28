from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio', methods=['POST'])
def audio():
    with open('./tmp/audio.wav', 'wb') as f:
        f.write(request.data)

    """
    predict uses the tensorflow model to predict 
    !! need to install tensorflow 
    """
    #print (predict( 'tmp/audio.wav' ))
    
    return


"""

def predict( voice )
    def random( voice ):
        X, sample_rate = librosa.load( voice , res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
        sample_rate = np.array(sample_rate)
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)
        feature = mfccs
        return feature

    feature = random(voice)
    x_t = feature.reshape(1,x.shape[0],1)

    #load model
    
    pred = model.predict(x_t)
    pred = np.argmax(pred)
    pred = np.reshape(pred, (1,))

    #load label binarizer instance
    lb = pickle.load(open( 'saved_lb.sav' , 'rb' ))
    emotion = lb.inverse_transform(pred)[0]
    return emotion


"""

if __name__ == "__main__":
    app.run(debug=True)
