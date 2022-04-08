import java.sql.*;

public class Main {
    Connection con;

    public void BookList() {
        String Driver = "";
        String url = "jdbc:mysql://localhost:3306/kdh?&serverTimezone=Asia/Seoul";
        String userid = "root";
        String pwd = "rusiper60";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("드라이버 로드 성공");
            System.out.println("DB 연결 준비");
            this.con = DriverManager.getConnection(url, userid, pwd);
            System.out.println("DB 연결 성공");

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    private void sqlRun() {
        String query = "SELECT * FROM book";
        try {
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Main main = new Main();

        main.BookList();
        main.sqlRun();
    }
}
