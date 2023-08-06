
export function sortTableByColumn(table, column, asc = true) {

    const dirModifier = asc? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelecterAll("tr"));


    //sort each row

    const sortedRows = rows.sort((a, b) => {
        console.log(a);
        console.log(b);
    });

}

sortTableByColumn(document.querySelector('table'), 1);
