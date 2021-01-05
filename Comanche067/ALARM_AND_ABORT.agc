### FILE="Main.annotation"
## Copyright:	Public domain.
## Filename:    ALARM_AND_ABORT.agc
## Purpose:	Part of the source code for Comanche 67 (Colossus 2C),
##		the one-and-only software release for the Apollo Guidance 
##		Computer (AGC) of Apollo 12's command module.  In the 
##		absence of a contemporary assembly listing for Comanche 67, 
##		the intention is to reconstruct the source code from a 
##		Comanche 55 (Colossus 2A, Apollo 11 CM) baseline and 
##		contemporary documentation describing the differences 
##		between the two.  Page numbers listed in the program 
##		comments follow Comanche 55 unless otherwise noted.
## Assembler:	yaYUL
## Contact:	Ron Burkey <info@sandroid.org>.
## Website:	www.ibiblio.org/apollo.
## Mod history: 2020-12-25 RSB	Began adaptation from Comanche 55 baseline.
##              2020-12-28 MAS	Implemented PCR 802.1, and fixed the CCSHOLE
##                            	alarm code which had been missed as part of
##                            	PCR 801.1.
##		2021-01-05 RSB	Adapted for use with preprocessor in 
##				reconstruction process.

## Page 1493
# THE FOLLOWING SUBROUTINE MAY BE CALLED TO DISPLAY A NON-ABORTIVE ALARM CONDITION.  IT MAY BE CALLED
# EITHER IN INTERRUPT OR UNDER EXECUTIVE CONTROL.
#
# CALLING SEQUENCE IS AS FOLLOWS:
#		TC	ALARM
#		OCT	NNNNN
#					(RETURNS HERE)

		BLOCK	02
		SETLOC	FFTAG7
		BANK

		EBANK=	FAILREG

		COUNT	02/ALARM

# ALARM TURNS ON THE PROGRAM ALARM LIGHT, BUT DOES NOT DISPLAY.

ALARM		INHINT

		CA	Q
ALARM2		TS	ALMCADR
		INDEX	Q
		CA	0
BORTENT		TS	L

PRIOENT		CA	BBANK
 +1		EXTEND
		ROR	SUPERBNK	# ADD SUPER BITS.
		TS	ALMCADR +1

LARMENT		CA	Q		# STORE RETURN FOR ALARM
		TS	ITEMP1

		CA	LOC
		TS	LOCALARM
		CA	BANKSET
		TS	BANKALRM

CHKFAIL1	CCS	FAILREG		# IS ANYTHING IN FAILREG
		TCF	CHKFAIL2	# YES TRY NEXT REG
## <b>Reconstruction:</b> This code, down to the matching "End" annotation, has been heavily changed
## from Comanche 55 due to PCR 802.1, Save Alarm Data after "Error Reset". The changes make FAILREG +2
## always contain the most recent program alarm, and a corresponding change in PINBALL prevents the
## RSET key from erasing it.
		CA	L
		TS	FAILREG
		TCF	PROGLARM	# TURN ALARM LIGHT ON FOR FIRST ALARM

CHKFAIL2	CCS	FAILREG +1
		TCF	PROGLARM
		CA	L
		TS	FAILREG +1
## Page 1494
PROGLARM	LXCH	FAILREG +2	# STORE AS "MOST RECENT" ALARM CODE

		CS	DSPTAB +11D	# TURN ON PROGRAM ALARM IF OFF
## <b>Reconstruction:</b> End of reconstructed block.
		MASK	OCT40400
		ADS	DSPTAB +11D

MULTEXIT	XCH	ITEMP1		# OBTAIN RETURN ADDRESS IN A
		RELINT
		INDEX	A
		TC	1

## <b>Reconstruction:</b> A chunk of code labeled "MULTFAIL" is defined here in Comanche 55. It has
## been removed as part of PCR 802.1.

# PRIOLARM DISPLAYS V05N09 VIA PRIODSPR WITH 3 RETURNS TO THE USER FROM THE ASTRONAUT AT CALL LOC +1,+2,+3 AND
# AN IMMEDIATE RETURN TO THE USER AT CALL LOC +4.  EXAMPLE FOLLOWS,
#		CAF	OCTXX		ALARM CODE
#		TC	BANKCALL
#		CADR	PRIOLARM

#		...	...
#		...	...
#		...	...		ASTRONAUT RETURN
#		TC	PHASCHNG	IMMEDIATE RETURN TO USER.  RESTART
#		OCT	X.1		PHASE CHANGE FOR PRIO DISPLAY

		BANK	10
		SETLOC	DISPLAYS
		BANK

		COUNT	10/DSPLA
PRIOLARM	INHINT			# * * * KEEP IN DISPLAY ROUTINES BANK
		TS	L		# SAVE ALARM CODE

		CA	BUF2		# 2 CADR OF PRIOLARM USER
		TS	ALMCADR
		CA	BUF2 +1
		TC	PRIOENT +1	# * LEAVE L ALONE
-2SEC		DEC	-200		# *** DONT MOVE
		CAF	V05N09
		TCF	PRIODSPR

## Page 1495

		BLOCK	02
		SETLOC	FFTAG13
		BANK

		COUNT	02/ALARM
		
BAILOUT		INHINT
		CA	Q
		TS	ALMCADR
		
		TC	BANKCALL
		CADR	VAC5STOR
		
		INDEX	ALMCADR
		CAF	0
		TC	BORTENT
OCT40400	OCT	40400

		INHINT
WHIMPER		CA	TWO
		AD	Z
		TS	BRUPT
		RESUME
		TC	POSTJUMP	# RESUME SENDS CONTROL HERE
		CADR	ENEMA
		
		SETLOC	FFTAG7
		BANK
		
POODOO		INHINT
		CA	Q
		TS	ALMCADR

		TC	BANKCALL
		CADR	VAC5STOR	# STORE ERASABLES FOR DEBUGGING PURPOSES.
		
		INDEX	ALMCADR
		CAF	0
ABORT2		TC	BORTENT
OCT77770	OCT	77770		# DONT MOVE
		CA	V37FLBIT	# IS AVERAGE G ON
		MASK	FLAGWRD7
		CCS	A
		TC	WHIMPER -1	# YES.  DONT DO POODOO.  DO BAILOUT.

		TC	DOWNFLAG
		ADRES	STATEFLG
		
		TC	DOWNFLAG
		
## Page 1496
		ADRES	REINTFLG
		
		TC	DOWNFLAG
		ADRES	NODOFLAG
		
		TC	BANKCALL
		CADR	MR.KLEAN
		TC	WHIMPER
		
CCSHOLE		INHINT
		CA	Q
		TS	ALMCADR
		TC	BANKCALL
		CADR	VAC5STOR
## <b>Reconstruction:<b>  The following line loaded "OCT1103" instead of "OCT21103" in Comanche 55.
## The change is due to PCR801.1.		
		CA	OCT21103
		TC	ABORT2
## <b>Reconstruction:<b>  The following constant was <code>OCT1103 OCT 1103</code> in Comanche 55.
## The change is due to PCR801.1.		
OCT21103	OCT	21103
CURTAINS	INHINT
		CA	Q
		TC	ALARM2
OCT217		OCT	00217
		TC	ALMCADR		# RETURN TO USER

DOALARM		EQUALS	ENDOFJOB

# CALLING SEQUENCE FOR VARALARM
#
#		CAF	(ALARM)
#		TC	VARALARM

# VARALARM TURNS ON PROGRAM ALARM LIGHT BUT DOES NOT DISPLAY

VARALARM	INHINT

		TS	L		# SAVE USERS ALARM CODE

		CA	Q		# SAVE USERS Q
		TS	ALMCADR

		TC	PRIOENT
OCT14		OCT	14		# DONT MOVE

		TC	ALMCADR		# RETURN TO USER

ABORT		EQUALS	BAILOUT		# *** TEMPORARY UNTIL ABORT CALLS OUT
