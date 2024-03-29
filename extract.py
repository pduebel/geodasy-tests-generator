def extract(db_file, test, proj):

    import pyodbc

    final_test_data = []

    odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;'%(db_file)
    conn = pyodbc.connect(odbc_conn_str)
    cursor = conn.cursor()

    
    if test == "SPT":

        hole_select = "select distinct HOLE_ID from SPT where PROJ_ID='%s'"%(proj)
        cursor.execute(hole_select)
        holes = cursor.fetchall()
        final_holes = [list(i) for i in holes]

        for i in range(len(final_holes)):
            data_select = "select SPT_BASE, SPT_N from %s where HOLE_ID='%s' and PROJ_ID='%s'"%(test, final_holes[i][0], proj)
            cursor.execute(data_select)
            data = cursor.fetchall()
            test_data = [list(i) for i in data]
            final_test_data.append(test_data)

    
    if test == "SHDP" or test == "DP":
        hole_select = "select distinct HOLE_ID from DPROBE where PROJ_ID='%s'"%(proj)
        cursor.execute(hole_select)
        holes = cursor.fetchall()
        final_holes = [list(i) for i in holes]

        for i in range(len(final_holes)):
            data_select = "select DPSTART, BLOWS from DPROBE where HOLE_ID='%s' and PROJ_ID='%s'"%(final_holes[i][0], proj)
            cursor.execute(data_select)
            data = cursor.fetchall()
            test_data = [list(i) for i in data]
            final_test_data.append(test_data)


    if test == "SV" or test == "HP":

        hole_select = "select distinct HOLE_ID from TRIALPIT where PROJ_ID='%s'"%(proj)
        cursor.execute(hole_select)
        holes = cursor.fetchall()
        final_holes = [list(i) for i in holes]

        if test == "HP":

            for i in range(len(final_holes)):
                data_select = """select TPIT_TEST_DEPTH, TPIT_AVERAGE_DFLT from TRIALPIT 
                                where (TPIT_TEST_TYPE='HP' or TPIT_TEST_TYPE='P' or TPIT_TEST_TYPE='HP>'
                                or TPIT_TEST_TYPE='HP<' or TPIT_TEST_TYPE='HP >' or TPIT_TEST_TYPE='HP <'
                                or TPIT_TEST_TYPE='H' or TPIT_TEST_TYPE='H>' or TPIT_TEST_TYPE='H >'
                                or TPIT_TEST_TYPE='H<' or TPIT_TEST_TYPE='H <' or TPIT_TEST_TYPE='P>'
                                or TPIT_TEST_TYPE='P >' or TPIT_TEST_TYPE='P<' or TPIT_TEST_TYPE='P <')
                                and HOLE_ID='%s' and PROJ_ID='%s'"""%(final_holes[i][0], proj)
                cursor.execute(data_select)
                data = cursor.fetchall()
                test_data = [list(i) for i in data]
                final_test_data.append(test_data)

        if test == "SV":

             for i in range(len(final_holes)):
                data_select = """select TPIT_TEST_DEPTH, TPIT_AVERAGE_DFLT from TRIALPIT 
                                where (TPIT_TEST_TYPE='SV' or TPIT_TEST_TYPE='V' or TPIT_TEST_TYPE='SV>'
                                or TPIT_TEST_TYPE='SV<' or TPIT_TEST_TYPE='SV >' or TPIT_TEST_TYPE='SV <'
                                or TPIT_TEST_TYPE='S' or TPIT_TEST_TYPE='S>' or TPIT_TEST_TYPE='S >'
                                or TPIT_TEST_TYPE='S<' or TPIT_TEST_TYPE='S <' or TPIT_TEST_TYPE='V>'
                                or TPIT_TEST_TYPE='V >' or TPIT_TEST_TYPE='V<' or TPIT_TEST_TYPE='V <')
                                and HOLE_ID='%s' and PROJ_ID='%s'"""%(final_holes[i][0], proj)
                cursor.execute(data_select)
                data = cursor.fetchall()
                test_data = [list(i) for i in data]
                final_test_data.append(test_data)

    cursor.commit()

    return final_holes, final_test_data





