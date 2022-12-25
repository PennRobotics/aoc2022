#include <math.h>

#define  DEBUG(s,v)  do{if(1){printf(s, v);}}while(0)

int main() {
  FILE *fh = open("input25", "r");
  while(fh) {
    n = 0;
    do {
      char ch = fh.readbytes();  // TODO: store as char array and reverse order
      uint8_t place = 0;
      uint64_t val;
      switch(ch) {
        case '=':
          val = -2;
          break;
        case '-':
          val = -1;
          break;
        case '0':
          val = 0;
          break;
        case '1':
          val = 1;
          break;
        case '2':
          val = 2;
          break;
      }
      n += powl(5, place) * val;
    } while (ch != '\n');
    DEBUG("%lld\n", n)
  }

  printf("Part A: %lld\n", 0);
  printf("Part B: %lld\n", 0);
}
