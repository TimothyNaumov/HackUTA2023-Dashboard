

const getStats = async (populateStats) => {

    await fetch('http://localhost:3001/api/stats')
        .then(res => res.json())
        .then(data => populateStats(data))
}
