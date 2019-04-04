<template>
    <div class='wrapper'>
        <h2>Project 1: Sudoku Solver</h2>
        <div class='container'>
            <br><br>
            <div class='info'>
                <div class='list--problems'>
                    <ul>
                        <li class='item--problem' 
                            v-for="item in questions" 
                            :key='item.id'
                            :class="{ active: item.active }">
                            {{ item.title }}
                        </li>
                    </ul>

                    <button>Solve!</button>
                </div>
                <div class='status'>
                    <h5>Messages: </h5>
                </div>
            </div>
            <div class='board'>
                    <ul>
                        <li class='cell'
                            v-for='cell in questions[0].cells'
                            :key='cell'>
                            <span class='cell-content'>{{ cell }}</span>
                        </li>
                    </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Sudoku',
    data: function() {
        return {
            questions: [
                { 
                    id: 1, 
                    title: 'Problem 1', 
                    active: true, 
                    cells: {
                        A1: 2,
                        A2: undefined,
                        A3: undefined, 
                        A4: undefined, 
                        A5: undefined, 
                        A6: undefined,
                        A7: undefined, 
                        A8: undefined, 
                        A9: undefined,
                        B1: undefined,
                        B2: undefined,
                        B3: undefined, 
                        B4: undefined, 
                        B5: undefined, 
                        B6: 6,
                        B7: 2, 
                        B8: undefined, 
                        B9: undefined,
                        C1: undefined,
                        C2: undefined,
                        C3: 1, 
                        C4: undefined, 
                        C5: undefined, 
                        C6: undefined,
                        C7: undefined, 
                        C8: 7, 
                        C9: undefined,
                        D1: undefined,
                        D2: undefined,
                        D3: 6, 
                        D4: undefined, 
                        D5: undefined, 
                        D6: 8,
                        D7: undefined, 
                        D8: undefined, 
                        D9: undefined,
                        E1: 3,
                        E2: undefined,
                        E3: undefined, 
                        E4: undefined, 
                        E5: 9, 
                        E6: undefined,
                        E7: undefined, 
                        E8: undefined, 
                        E9: 7,
                        F1: undefined,
                        F2: undefined,
                        F3: undefined, 
                        F4: 6, 
                        F5: undefined, 
                        F6: undefined,
                        F7: 4, 
                        F8: undefined, 
                        F9: undefined,
                        G1: undefined,
                        G2: 4,
                        G3: undefined, 
                        G4: undefined, 
                        G5: undefined, 
                        G6: undefined,
                        G7: 8, 
                        G8: undefined, 
                        G9: undefined,
                        H1: undefined,
                        H2: undefined,
                        H3: 5, 
                        H4: 2, 
                        H5: undefined, 
                        H6: undefined,
                        H7: undefined, 
                        H8: undefined, 
                        H9: undefined,
                        I1: undefined,
                        I2: undefined,
                        I3: undefined, 
                        I4: undefined, 
                        I5: undefined, 
                        I6: undefined,
                        I7: undefined, 
                        I8: undefined, 
                        I9: 3,
                    }
                }, 
                { id: 2, title: 'Problem 2', active: false },
            ]
        }
    }
   
}
</script>


<style scoped>
h2 {
    padding: 30px 0;
}

.container {
    display: flex; 
    flex-direction: row;

}

.board {
    flex-wrap: wrap;
    width: 540px;
    background-color: #ddd;
    padding: 10px 0 0 10px;
}

.cell {
    position: relative;
    list-style: none;
    height: 30px;
    width: 30px;
    display: inline-block;
    margin: 0 10px 10px 0;
    background-color: white;
    padding: 10px;
    text-align: center;
}

.cell-content {
    position: absolute;
    text-align: center;
    line-height: 30px;
    font-size: 30px;
    left: 20px;
}

.info {
    display: flex;
    flex-direction: column;
    margin: 0 30px 0 0;
}

.status { 
    border-top: 1px solid gray;
}

ul {
    margin: 0;
    padding: 0;
}

.item--problem {
    border: 1px solid #222; 
    margin-bottom: 15px;
    list-style: none;
    padding: 15px;
    display: block;
    cursor: pointer;
}

.item--problem.active {
    background: gray; 
    color: white; 
    font-weight: 800;
}

.item--problem:hover {
    background: gray; 
    color: white;
}
</style>