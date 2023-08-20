import pickle

def load_model():

    file = open("../models/model.pkl", "rb")
    model = pickle.load(file)
    file.close() 

    return model


def load_encoder():

    file = open("../models/ohe.pkl", "rb")
    encoder = pickle.load(file)
    file.close() 

    return encoder