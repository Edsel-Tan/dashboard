$(document).ready(function() {
    // Function to parse CSV correctly (handles quoted commas)
    function parseCSV(csvString) {
        const rows = [];
        const regex = /(".*?"|[^",\s]+)(?=\s*,|\s*$)/g;
        const lines = csvString.split('\n');

        lines.forEach(line => {
            const matches = [];
            let match;
            while ((match = regex.exec(line)) !== null) {
                let value = match[1];
                if (value.startsWith('"') && value.endsWith('"')) {
                    value = value.slice(1, -1).replace(/""/g, '"'); // Handle escaped quotes
                }
                matches.push(value);
            }
            rows.push(matches);
        });

        return rows;
    }

    // Fetch the CSV file
    $.get('solution_metadata.csv', function(data) {
        const parsedCSV = parseCSV(data);

        // Extract headers
        const headers = parsedCSV[0];

        // Append headers to the table
        headers.forEach(header => {
            $('#solutionsTable thead tr').append(`<th>${header.trim()}</th>`);
        });

        // Append rows to the table body
        parsedCSV.slice(1).forEach(row => {
            if (row.length > 1) { // Ignore empty lines
                const rowHTML = row.map(cell => `<td>${cell.trim()}</td>`).join('');
                $('#solutionsTable tbody').append(`<tr>${rowHTML}</tr>`);
            }
        });

        // Initialize DataTables with a row callback to color rows
        $('#solutionsTable').DataTable({
	    'pageLength': 50,
	    'aLengthMenu': [[25, 50, 75, -1], [25, 50, 75, 'All']],
	    columnDefs: [
                {
                    targets: 0, // Enable search only for the first column
                    searchable: true
                },
		{
                    targets: '_all', // Target all columns
                    searchable: false // Disable search for all columns by default
                }
            ],


	    rowCallback: function(row, data, index) {
                // Get the value from the 3rd column (index 2 since it's zero-based)
                const value = parseFloat(data[2]);

                // Apply colors based on value
                if (value > 240) {
                    $(row).css('background-color', 'red'); // High values
                } else if (value > 60) {
                    $(row).css('background-color', 'yellow'); // Medium values
                } else {
                    $(row).css('background-color', 'green'); // Low values
                }
            }
        });
    });
});

