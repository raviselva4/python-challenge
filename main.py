import os
import csv
import sys
import time
#import pprint

#       sub module used for both PyBank Module and PyPoll Module.....
#
def opencsv(path, option):
    avgchange  = []
    totalrows  = 0
    totalamt   = 0
    amount     = 0
    camount    = 0
    preamount  = 0
    profit_change = {}
    poll_dict  = {}
    pline = "-----------------------------------------------------"
    with open(path) as csvfile:
        csvreader  = csv.reader(csvfile, delimiter=',')
        csvheader  = next(csvreader)

        for row in csvreader:
            if option == 1:
                #  To process PyBank module data...
                amount = int(row[1])
                totalrows += 1
                totalamt  += amount
                camount = amount-preamount
                if totalrows == 1:
                    preamount  = amount
                elif totalrows > 1:
                    avgchange.append(camount)
                    preamount = amount
                    profit_change.update({row[0]:(camount)})
                    
            elif option == 2:
                #  To process PyPoll module data...
                totalrows += 1
                if totalrows == 1:
                    poll_dict = {row[2]:1}
                elif row[2] in poll_dict:
                    poll_dict[row[2]] += 1
                else:
                    poll_dict.update({row[2]:1})
        
        if option == 1:
            #           PyBank Module data manupluation......
            #
            #print(profit_change)
            #print(avgchange)
            maxkey = max(profit_change, key=profit_change.get)
            minkey = min(profit_change, key=profit_change.get)
            maxval = profit_change[maxkey]
            minval = profit_change[minkey]
            #print("Maxkey" + maxkey)
            #print("Min. Key" + minkey)
            printlist = {
                "Heading":"Financial Analysis",
                "Line": pline,
                "Line1": ["Total Months :", totalrows],
                "Line2": ["Total :", totalamt],
                "Line3": ["Average Change", round(sum(avgchange)/len(avgchange),2)],
                "Line4": ["Greatest Increase in Profits :", maxkey ,maxval],
                "Line5": ["Greatest Decrease in Profits :", minkey ,minval]
            }
            #print(pline)
            #print('${:,d}'.format(totalamt))
            return printlist
        elif option == 2:
            #               PyPoll Module data manupulation and printing...
            #
            #   defining output file for PyPoll module....
            #
            output_path = os.path.join('PyPoll','poll_analysis.txt')
            txtfile = open(output_path, 'w')
            #print("work in progress....")
            #print(poll_dict)
            #                   only works with mac..  for windows need to replace "clear" with "cls"
            os.system("clear")
            #   Print output to the screen and file......
            print("Election Results")
            print("Election Results" ,file=txtfile)
            print(pline)
            print(pline ,file=txtfile)
            print("Total Votes: "+ str(totalrows))
            print("Total Votes: "+ str(totalrows) ,file=txtfile)
            print(pline)
            print(pline ,file=txtfile)
            maxkey = max(poll_dict, key=poll_dict.get)
            for key, value in poll_dict.items():
                print(key,': ' +str('{:.3f}'.format(round((value*100/totalrows),3)))+'%', '('+str(value)+')')
                print(key,': ' +str('{:.3f}'.format(round((value*100/totalrows),3)))+'%', '('+str(value)+')', file=txtfile)
            print(pline)
            print(pline ,file=txtfile)
            print("Winner: " + maxkey)
            print("Winner: " + maxkey ,file=txtfile)
            print(pline)
            print(pline ,file=txtfile)
            txtfile.close()
            return
#--------------------------------------------------------------------------------------------------------------
#                       Main program starts here........
#--------------------------------------------------------------------------------------------------------------
answer = 0
#                   Display Menu and Validate input (accept only 1/2/3).....
while answer < 3:
    while True:
        try:
            print(" 1. Do Financial Analysis")
            print(" 2. Do Poll Analysis")
            print(" 3. Exit ")
            print(" ")
            answer = int(input("Enter your options (1/2/3) :"))
            if answer == 1:
                #   Passing path and datafile...
                csvpath_bank = os.path.join('PyBank','Resources','budget_data.csv')
                #   Calling sub module with datafile path and option (which module)...
                printlist2 = opencsv(csvpath_bank, answer)
                #print(printlist2)
                #                   only works with mac..  for windows need to replace "clear" with "cls"
                os.system("clear")
                #   Print output to the screen......
                print(printlist2["Heading"])
                print(printlist2["Line"])
                #
                print(f'{printlist2["Line1"][0]} {printlist2["Line1"][1]} ')
                print(f'{printlist2["Line2"][0]} ${printlist2["Line2"][1]} ')
                print(f'{printlist2["Line3"][0]} {printlist2["Line3"][1]} ')
                print(f'{printlist2["Line4"][0]} {printlist2["Line4"][1]}  (${printlist2["Line4"][2]})')
                print(f'{printlist2["Line5"][0]} {printlist2["Line5"][1]}  (${printlist2["Line5"][2]})')
                #
                # print output into text file....
                #
                output_path = os.path.join('PyBank','financial_analysis.txt')
                #with open(output_path, "w+") as txtfile:
                txtfile = open(output_path, 'w')
                print(printlist2["Heading"] , file=txtfile)
                print(printlist2["Line"] , file=txtfile)
                print(f'{printlist2["Line1"][0]} {printlist2["Line1"][1]} ' , file=txtfile)
                print(f'{printlist2["Line2"][0]} ${printlist2["Line2"][1]} ' , file=txtfile)
                print(f'{printlist2["Line3"][0]} {printlist2["Line3"][1]} ' , file=txtfile)
                print(f'{printlist2["Line4"][0]} {printlist2["Line4"][1]}  (${printlist2["Line4"][2]})' , file=txtfile)
                print(f'{printlist2["Line5"][0]} {printlist2["Line5"][1]}  (${printlist2["Line5"][2]})' , file=txtfile)
                txtfile.close()
                print(" ")
                print("  ")
                #   To display Main menu to the user...
                dummy = input("Press Enter to continue...")
                #                   only works with mac..  for windows need to replace "clear" with "cls"
                os.system("clear")
            elif answer == 2:
                #       Taking longer than opton 1, hence to inform the user processing is going on...
                print("Still in process....")
                print(" ")
                #   Passing path and datafile...
                csvpath_poll = os.path.join('PyPoll', 'Resources','election_data.csv')
                #   Calling sub module with datafile path and option (which module)...
                opencsv(csvpath_poll, answer)
                #   To display Main menu to the user...
                dummy = input("Press Enter to continue...")
                #                   only works with mac..  for windows need to replace "clear" with "cls"
                os.system("clear")
            elif answer == 3:
                print(" ")
                print("Thanks for using this program. Goodbye...")
                sys.exit()
            else:
                print("Valid Options are 1 or 2 or 3. Please Re-try again!!!")
                time.sleep(1)
                #                   only works with mac..  for windows need to replace "clear" with "cls"
                os.system("clear")
                True
        except ValueError:
            print("Valid Options are 1 or 2 or 3. Please Re-try again!!!")
            time.sleep(1)
            #                   only works with mac..  for windows need to replace "clear" with "cls"
            os.system("clear")
            answer = 5
            True


