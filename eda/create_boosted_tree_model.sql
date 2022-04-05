CREATE OR REPLACE MODEL
  human_stress_classification OPTIONS(model_type='BOOSTED_TREE_CLASSIFIER',
    input_label_cols=['sl']) AS
SELECT
  sr, rr, t, lm, bo, rem, sh, hr, sl
FROM
  `human_stress_detection`;
