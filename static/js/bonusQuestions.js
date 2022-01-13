// you receive an array of objects which you must sort in the by the key "sortField" in the "sortDirection"
function getSortedItems(items, sortField, sortDirection) {
    console.log(items)
    console.log(sortField)
    console.log(sortDirection)

    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //

    console.log(items[0][sortField])
    if (sortDirection === "asc" && (sortField == "VoteCount" || sortField == "ViewNumber")) {
        items.sort((function (a, b) {return a[sortField] - b[sortField]}))
    } else if (sortDirection === "desc" && (sortField == "VoteCount" || sortField == "ViewNumber")) {
        items.sort((function (a, b) {return b[sortField] - a[sortField]}))
    } else if (sortDirection === "asc" && (sortField === "Title" || sortField === "Description")) {
        items.sort(function (a, b) {
            if (a[sortField] < b[sortField]) {return -1}
            else if (a[sortField] > b[sortField]) {return  1}
            else {return 0}
        })
    } else if (sortDirection === "desc" && (sortField === "Title" || sortField === "Description")) {
        items.sort(function (a, b) {
            if (a[sortField] > b[sortField]) {return -1}
            else if (a[sortField] < b[sortField]) {return  1}
            else {return 0}
        })
    }

    return items
}

// you receive an array of objects which you must filter by all it's keys to have a value matching "filterValue"
function getFilteredItems(items, filterValue) {
    console.log(items)
    console.log(filterValue)
    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //
    let reverse = false
    if (filterValue[0]=="!") {
        reverse = true
        filterValue = filterValue.substring(1)
    }
    let reverse_filtered_items = items
    console.log(items)
    let filtered_items = []
    for (let i=0; i<items.length; i++) {
        if ((items[i]["Title"].includes(filterValue) || items[i]["Description"].includes(filterValue)) && !reverse) {
            filtered_items.push(items[i])
        } else if (items[i]["Title"].includes(filterValue) || items[i]["Description"].includes(filterValue)) {
            delete reverse_filtered_items[i]
        }
    }
    let refined_reverse = []
    if (reverse) {
        for (let index=0; index<reverse_filtered_items.length; index++){
            if (reverse_filtered_items[index]) {
                refined_reverse.push(reverse_filtered_items[index])
            }
        }
        return refined_reverse
    } else {
        return filtered_items
    }
}

function toggleTheme() {
    console.log("toggle theme")
}

function increaseFont() {
    console.log("increaseFont")
}

function decreaseFont() {
    console.log("decreaseFont")
}