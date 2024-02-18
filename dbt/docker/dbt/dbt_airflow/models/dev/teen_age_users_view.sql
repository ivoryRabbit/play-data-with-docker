
-- Use the `ref` function to select from other models

{{ config(materialized='view') }}
SELECT *
FROM {{ ref("users") }}
WHERE age BETWEEN 10 AND 19
