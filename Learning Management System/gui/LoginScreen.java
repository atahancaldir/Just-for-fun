package gui;

import javax.swing.*;
import java.awt.*;

import model.Department;

public class LoginScreen extends JFrame{
    private Department department;

    public LoginScreen(Department department){
        this.department = department;

        this.setSize(300,150);
        this.setTitle("Login");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLocationRelativeTo(null);

        JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 20));
        panel.setBackground(new Color(51,85,144));
        this.add(panel);

        JLabel label = new JLabel("Email: ");
        label.setFont(new Font("Verdana", Font.BOLD, 15));
        label.setForeground(Color.WHITE);
        panel.add(label);

        JTextField textField = new JTextField();
        textField.setColumns(20);
        panel.add(textField);

        JButton button = new JButton("Login");
        panel.add(button);

        JLogin loginListener = new JLogin(textField, department);
        button.addActionListener(loginListener);

        this.setVisible(true);
    }
}
