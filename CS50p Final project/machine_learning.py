from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def main():
    train_ml_model()


def train_ml_model(ex, ex_answer):

    f_encoder = [LabelEncoder() for _ in range(5)]
    ex_encoded = [list(f_encoder[i].fit_transform(col)) for i, col in enumerate(zip(*ex))]
    ex_encoded =list(zip(*ex_encoded))

    t_encoder = LabelEncoder()
    answer_encoded = t_encoder.fit_transform(ex_answer)

    model = DecisionTreeClassifier()
    model.fit(ex_encoded, answer_encoded)

    return model, f_encoder, t_encoder


if __name__ == "__main__":
    main()
