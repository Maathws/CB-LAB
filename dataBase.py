from dotenv import load_dotenv
import os
import mysql.connector
import retornaDicionarioErp as dicerp

load_dotenv()

def conectarDataBaseGeral():
    try:
        conexaoDB = mysql.connector.connect(
            host = os.getenv("DATABASE_HOST"),
            port = os.getenv("DATABASE_PORT"),
            user = os.getenv("DATABASE_USER"),
            password = os.getenv("DATABASE_PASSWORD")
        )
        print('Conexao bem sucedida')
        return conexaoDB
    
    except mysql.connector.Error as e:
        print(f'Erro na conexao com o banco de dados: {e}')


def criarDataBaseRestaurantesETabelas(conexaoDB):
    try:
        cursor = conexaoDB.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS restauranteasanorte;")
        print('Banco de dados restauranteasanorte criado ou já existente')

        cursor.execute("USE restauranteasanorte")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS guest_checks (
            guest_check_id BIGINT PRIMARY KEY,
            chk_num INT,
            opn_bus_dt DATE,
            opn_utc DATETIME,
            clsd_bus_dt DATE,
            clsd_utc DATETIME,
            last_trans_utc DATETIME,
            last_updated_utc DATETIME,
            clsd_flag BOOLEAN,
            gst_cnt INT,
            sub_ttl DECIMAL(10, 2),
            chk_ttl DECIMAL(10, 2),
            dsc_ttl DECIMAL(10, 2),
            pay_ttl DECIMAL(10, 2),
            rvc_num INT,
            ot_num INT,
            tbl_num INT,
            tbl_name VARCHAR(50),
            emp_num INT,
            num_srvc_rd INT,
            num_chk_prntd INT
        )
        """)
        print('Tabela guest_checks criada ou já existente')

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_item (
            menu_item_id BIGINT PRIMARY KEY,
            guest_check_id BIGINT,
            line_id BIGINT,
            mi_num INT,
            incl_tax DECIMAL(10, 2),
            prc_lvl INT,
            discount DECIMAL(10, 2) DEFAULT NULL,
            service_charge DECIMAL(10, 2) DEFAULT NULL,
            tender_media VARCHAR(255) DEFAULT NULL,
            error_code VARCHAR(255) DEFAULT NULL,
            FOREIGN KEY (guest_check_id) REFERENCES guest_checks(guest_check_id)
        )
        """)
        print('Tabela menu_item criada ou já existente')


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS taxes (
            tax_num INT PRIMARY KEY,
            guest_check_id BIGINT,
            txbl_sls_ttl DECIMAL(10, 2),
            tax_coll_ttl DECIMAL(10, 2),
            tax_rate DECIMAL(5, 2),
            type INT,
            FOREIGN KEY (guest_check_id) REFERENCES guest_checks(guest_check_id)
        )
        """)
        print('Tabela taxes criada ou já existente')


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS detail_lines (
            detail_line_id BIGINT PRIMARY KEY,
            guest_check_id BIGINT,
            guest_check_line_item_id BIGINT,
            detail_utc DATETIME,
            detail_lcl DATETIME,
            last_update_utc DATETIME,
            bus_dt DATE,
            ws_num INT,
            dsp_ttl DECIMAL(10, 2),
            dsp_qty INT,
            agg_ttl DECIMAL(10, 2),
            agg_qty INT,
            chk_emp_id INT,
            chk_emp_num INT,
            svc_rnd_num INT,
            seat_num INT,
            menu_item_id BIGINT,
            FOREIGN KEY (menu_item_id) REFERENCES menu_item(menu_item_id)
        )
        """)
        print("Tabela detail_lines criada ou já existente")

        print("Banco de dados e tabelas criados com sucesso")

    except mysql.connector.Error as e:
        print(f"Erro ao criar banco de dados ou tabela: {e}")

    finally:
        cursor.close()



def inserirDataBaseRestaurantesETabelas(conexaoDB, dicionarioErp):
    try:
        cursor = conexaoDB.cursor()

        for guest_check in dicionarioErp['guestChecks']:
            cursor.execute("""
            INSERT INTO guest_checks (
                guest_check_id, chk_num, opn_bus_dt, opn_utc, clsd_bus_dt, clsd_utc,
                last_trans_utc, last_updated_utc, clsd_flag, gst_cnt, sub_ttl, chk_ttl,
                dsc_ttl, pay_ttl, rvc_num, ot_num, tbl_num, tbl_name, emp_num, num_srvc_rd,
                num_chk_prntd
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                guest_check['guestCheckId'], guest_check['chkNum'], guest_check['opnBusDt'],
                guest_check['opnUTC'], guest_check['clsdBusDt'], guest_check['clsdUTC'],
                guest_check['lastTransUTC'], guest_check['lastUpdatedUTC'], guest_check['clsdFlag'],
                guest_check['gstCnt'], guest_check['subTtl'], guest_check['chkTtl'],
                guest_check['dscTtl'], guest_check['payTtl'], guest_check['rvcNum'],
                guest_check['otNum'], guest_check['tblNum'], guest_check['tblName'],
                guest_check['empNum'], guest_check['numSrvcRd'], guest_check['numChkPrntd']
            ))
            conexaoDB.commit()

            if guest_check['taxes']:
                for tax in guest_check['taxes']:
                    cursor.execute("""
                    INSERT INTO taxes (
                        tax_num, guest_check_id, txbl_sls_ttl, tax_coll_ttl, tax_rate, type
                    ) VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        tax['taxNum'], guest_check['guestCheckId'], tax['txblSlsTtl'],
                        tax['taxCollTtl'], tax['taxRate'], tax['type']
                    ))
                conexaoDB.commit()


            for detail in guest_check['detailLines']:
                menu_item = detail['menuItem']

                cursor.execute("""
                INSERT INTO menu_item (
                    menu_item_id, guest_check_id, line_id, mi_num, incl_tax, prc_lvl, discount,
                    service_charge, tender_media, error_code
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    menu_item['miNum'], guest_check['guestCheckId'], detail['lineNum'],
                    menu_item['miNum'], menu_item['inclTax'], menu_item['prcLvl'],
                    menu_item.get('discount', None), menu_item.get('serviceCharge', None),
                    menu_item.get('tenderMedia', None), menu_item.get('errorCode', None)
                ))
                conexaoDB.commit()


            for detail in guest_check['detailLines']:
                menu_item = detail['menuItem']

                cursor.execute("""
                INSERT INTO detail_lines (
                    detail_line_id, guest_check_id, guest_check_line_item_id, detail_utc, detail_lcl, last_update_utc,
                    bus_dt, ws_num, dsp_ttl, dsp_qty, agg_ttl, agg_qty, chk_emp_id, chk_emp_num,
                    svc_rnd_num, seat_num, menu_item_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    detail['guestCheckLineItemId'], guest_check['guestCheckId'], detail['guestCheckLineItemId'], detail['detailUTC'],
                    detail['detailLcl'], detail['lastUpdateUTC'], detail['busDt'], detail['wsNum'],
                    detail['dspTtl'], detail['dspQty'], detail['aggTtl'], detail['aggQty'],
                    detail['chkEmpId'], detail['chkEmpNum'], detail['svcRndNum'],
                    detail['seatNum'], menu_item['miNum']
                ))

                conexaoDB.commit()

            print("Dados inseridos com sucesso")

    except mysql.connector.Error as e:
        print(f"Erro ao inserir dados: {e}")

    finally:
        cursor.close()




conexaoDB = conectarDataBaseGeral()
criarDataBaseRestaurantesETabelas(conexaoDB)

dicionarioErp = dicerp.retornaDicionarioErp()

inserirDataBaseRestaurantesETabelas(conexaoDB, dicionarioErp)