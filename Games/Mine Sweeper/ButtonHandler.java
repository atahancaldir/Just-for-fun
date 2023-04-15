import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class ButtonHandler extends MouseAdapter implements ActionListener {
    private int row;
    private int column;
    private MineGrid mineGrid;

    public ButtonHandler(int row, int column, MineGrid mineGrid) {
        this.row = row;
        this.column = column;
        this.mineGrid = mineGrid;
    }

    public void mouseClicked(MouseEvent mouseEvent){
        if(mouseEvent.getButton() == 3) {
            if (!this.mineGrid.isFlagged(row, column) && ((JButton) mouseEvent.getSource()).getText().equals("")) {
                ((JButton) mouseEvent.getSource()).setText("F");
                this.mineGrid.changeFlag(row, column);
                this.mineGrid.checkFlags();
            }
            else if(this.mineGrid.isFlagged(row, column)){
                ((JButton) mouseEvent.getSource()).setText("");
                this.mineGrid.changeFlag(row, column);
            }
        }
    }

    public void actionPerformed(ActionEvent actionEvent) {
        if (this.mineGrid.isMine(this.row, this.column)) {
            JOptionPane.showMessageDialog(null, "OOOPS!!");
            System.exit(0);
        } else {
            if (actionEvent.getSource() instanceof JButton) {
                ((JButton) actionEvent.getSource()).setText(String.valueOf(this.mineGrid.getCellContent(row, column)));
                if(this.mineGrid.isFlagged(row, column)){
                    this.mineGrid.changeFlag(row, column);
                }
                if(this.mineGrid.getCellContent(row, column) == 0){
                    this.openCell(row-1, column-1);
                    this.openCell(row-1, column);
                    this.openCell(row-1, column+1);

                    this.openCell(row, column-1);
                    this.openCell(row, column+1);

                    this.openCell(row+1, column-1);
                    this.openCell(row+1, column);
                    this.openCell(row+1, column+1);
                }
            }
        }
    }

    private void openCell(int row, int column){
        if(mineGrid.isInsideGrid(row, column)){
            mineGrid.getButton(row, column).setText(String.valueOf(this.mineGrid.getCellContent(row, column)));
        }
    }
}
