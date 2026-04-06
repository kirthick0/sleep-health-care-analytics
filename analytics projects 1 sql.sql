BULK INSERT sleep_health_data
FROM "C:\Users\kirthick\Downloads\analytics project\cleaned_data.csv"
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK,
    CODEPAGE = '65001'
);
GO