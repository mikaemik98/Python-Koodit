let numCandidates = parseInt(prompt("Enter the number of candidates:"));

let candidates = [];
for (let i = 0; i < numCandidates; i++) {
    let name = prompt(`Enter the name for candidate ${i + 1}:`);
    candidates.push({ name: name, votes: 0 });
}

let numVoters = parseInt(prompt("Enter the number of voters:"));

for (let i = 0; i < numVoters; i++) {
    let vote = prompt(`Voter ${i + 1}, who will you vote for? (Enter the candidate's name or leave blank for an empty vote):`);
    if (vote) {
        let candidate = candidates.find(candidate => candidate.name.toLowerCase() === vote.toLowerCase());
        if (candidate) {
            candidate.votes++;
        } else {
            console.log(`Invalid vote for '${vote}'. No candidate with this name.`);
        }
    }
}

candidates.sort((a, b) => b.votes - a.votes);
let winner = candidates[0];

console.log(`The winner is ${winner.name} with ${winner.votes} votes.`);
console.log("Results:");
candidates.forEach(candidate => {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
});