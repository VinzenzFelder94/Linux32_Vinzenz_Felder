#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"

#define GPIO3 0x481aE000
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_SETDATAOUT 0x194
#define P9_27 (1<<19)
unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3 + GPIO_CLEARDATAOUT);
unsigned int volatile * const GPIO3_SET   = (unsigned int *) (GPIO3 + GPIO_SETDATAOUT);

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	unsigned int i;

	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	for(i = 0; i < 20000000000000; i++) {
		*GPIO3_SET   = P9_27;
		__delay_cycles(0);

		*GPIO3_CLEAR = P9_27;
		__delay_cycles(0);
	}
	__halt();
}
