import javax.swing.*;
import java.util.Random;

public class MineGrid {
    private static final int MINE = -1;
    private int[][] mineInformation;
    private int[][] flagInformation;
    private JButton[][] buttons;

    public MineGrid(int numberOfRows, int numberOfColumns, int numberOfMines) {
        this.mineInformation = new int[numberOfRows][numberOfColumns];
        this.flagInformation = new int[numberOfRows][numberOfColumns];
        this.buttons = new JButton[numberOfRows][numberOfColumns];
        this.initializeCells();
        this.placeMines(numberOfMines);
        this.setMineInformation();
    }

    private void initializeCells() {
        for (int i = 0; i < this.mineInformation.length; ++i) {
            for (int j = 0; j < this.mineInformation[0].length; ++j) {
                this.mineInformation[i][j] = 0;
                this.flagInformation[i][j] = 0;
            }
        }
    }

    private void placeMines(int numberOfMines) {
        Random random = new Random();
        for (int i = 0; i < numberOfMines; ++i) {
            int row = random.nextInt(mineInformation.length);
            int column = random.nextInt(mineInformation[0].length);
            if (this.mineInformation[row][column] != MINE) {
                this.mineInformation[row][column] = MINE;
            } else {
                --i;
            }
        }
    }

    public boolean isMine(int row, int column) {
        return this.mineInformation[row][column] == MINE;
    }

    private void incrementMineCountAt(int row, int column) {
        if (this.isInsideGrid(row, column) && !this.isMine(row, column)) {
            ++this.mineInformation[row][column];
        }
    }

    private void setMineInformation() {
        for (int i = 0; i < this.mineInformation.length; ++i) {
            for (int j = 0; j < this.mineInformation[0].length; ++j) {
                if (this.mineInformation[i][j] == MINE) {
                    // previous row
                    this.incrementMineCountAt(i - 1, j - 1);
                    this.incrementMineCountAt(i - 1, j);
                    this.incrementMineCountAt(i - 1, j + 1);

                    // left and right cells
                    this.incrementMineCountAt(i, j - 1);
                    this.incrementMineCountAt(i, j + 1);

                    // next row
                    this.incrementMineCountAt(i + 1, j - 1);
                    this.incrementMineCountAt(i + 1, j);
                    this.incrementMineCountAt(i + 1, j + 1);
                }
            }
        }
    }

    public boolean isInsideGrid(int row, int column) {
        return (row >= 0 && row < this.mineInformation.length) &&
                (column >= 0 && column < this.mineInformation[0].length);
    }

    public int getCellContent(int row, int column) {
        return this.mineInformation[row][column];
    }

    public boolean isFlagged(int row, int column){
        return this.flagInformation[row][column] == 1;
    }

    public void changeFlag(int row, int column){
        if(isFlagged(row, column)){
            this.flagInformation[row][column] = 0;
        }
        else{
            this.flagInformation[row][column] = 1;
        }
    }

    public void checkFlags(){
        for (int i = 0; i < this.mineInformation.length; ++i) {
            for (int j = 0; j < this.mineInformation[0].length; ++j) {
                if(this.mineInformation[i][j] == MINE && this.flagInformation[i][j] == 0){
                    return;
                }
            }
        }
        JOptionPane.showMessageDialog(null, "“You’re a genius.");
        System.exit(0);
    }

    public void addButton(int row, int column, JButton button){
        buttons[row][column] = button;
    }

    public JButton getButton(int row, int column){
        return buttons[row][column];
    }
}
