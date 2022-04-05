SELECT
  *
FROM
  ML.EVALUATE(MODEL human_stress_classification,
    TABLE `human_stress_detection`);
