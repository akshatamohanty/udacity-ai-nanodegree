<template>
    <div class='container'>
        <h2>Project 1: Sudoku Solver</h2>
        <br><br>
        <div class='board'></div>
        <div class='info'>
            <div class='list--problems'>
            </div>
            <div class='status'>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Sudoku',
}
</script>


<style scoped>
.container {
    display: flex; 
    flex-direction: column;

    padding: 30px 0;
}

.board {
    border: 1px solid black;
    height: 150px; 
    width: 150px;
}

.info {
    border: 1px solid blue;
    width: 75px;
}
</style>