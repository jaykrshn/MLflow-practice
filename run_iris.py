import mlflow

parameters={
    "penality":"l2",
    "C":1.0
}

experiment_name = "Classifier"
entry_point = "LogisticRegression"

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    parameters=parameters,
    experiment_name=experiment_name
)