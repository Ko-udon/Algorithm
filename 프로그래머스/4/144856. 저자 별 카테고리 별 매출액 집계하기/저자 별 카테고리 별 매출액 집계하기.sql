# 확실히 어렵다

SELECT
    base.author_id,
    author.author_name,
    base.category,
    base.total_sales
FROM (
    SELECT
        b.author_id,
        b.category,
        SUM(b.price * bs.sales) AS total_sales
    FROM book_sales AS bs
    JOIN book AS b
        ON bs.book_id = b.book_id
    WHERE sales_date LIKE '2022-01%'
    GROUP BY b.author_id, b.category
) AS base
JOIN author 
    ON base.author_id = author.author_id
ORDER BY base.author_id, base.category DESC;