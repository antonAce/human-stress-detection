# Human stress detection in and through sleep

[![Made with Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)

A serverless application for human stress detection in and through sleep, hosted with Google Cloud Platform. **Note:** this is NOT a commercial project! All rights, including data and technology, belong to the [SaYoPillow organization](https://arxiv.org/abs/2007.07377). The project does not violate the terms and agreements provided by the author's license.

### Dataset

The [dataset page](https://www.kaggle.com/datasets/laavanya/human-stress-detection-in-and-through-sleep) on Kaggle. The goal of the research is to solve a supervised classification problem for predicting stress level using numerical features (multilabel classification problem). Featues used for classification: `snoring range of the user` (`sr`), `respiration rate` (`rr`), `body temperature` (`t`), `limb movement rate` (`lm`), `blood oxygen levels` (`bo`), `eye movement` (`rem`), `number of hours of sleep` (`sh`) and `heart rate` (`hr`). The label represents a certain stress level: `0` - Low or normal, `1` – Medium low, `2` - Medium, `3` - Medium high, `4` - High.

### Local run

GCP functions can be invoked locally using the Google Cloud SDK for Python, specifically the [functions-framework](https://pypi.org/project/functions-framework/) package, which is already included to the dependencies list. To run [Classifier HTTP Trigger](./src/functions/classifier) use following command:

```sh
functions-framework --target calculate_stress_level --debug
```

### Used GCP programming guides

 - [GCP HTTP Functions](https://cloud.google.com/functions/docs/writing/http);
 - [GCP HTTP method types](https://cloud.google.com/functions/docs/samples/functions-http-method);
 - [GCP Create and deploy a Python Cloud Function](https://cloud.google.com/functions/docs/create-deploy-python);
 - [GCP Host a static website](https://cloud.google.com/storage/docs/hosting-static-website);
