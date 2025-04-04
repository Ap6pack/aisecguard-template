import shap

class SHAPExplainer:
    def __init__(self, model):
        self.model = model
        self.explainer = shap.Explainer(model)

    def explain(self, X_sample):
        shap_values = self.explainer(X_sample)
        shap.summary_plot(shap_values, X_sample)
        return shap_values
