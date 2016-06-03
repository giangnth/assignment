select count(*) from (SELECT docid, SUM(count) as term_count, term FROM frequency GROUP BY term HAVING term_count >= 300);
