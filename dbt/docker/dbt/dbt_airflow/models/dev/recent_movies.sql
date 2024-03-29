
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized="table") }}

WITH source_data AS (
    SELECT *
    FROM {{ ref("movies") }}
    ORDER BY year DESC, id DESC
    LIMIT 100
)

SELECT *
FROM source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- WHERE id IS NOT NULL
