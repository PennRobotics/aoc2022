#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int digit_map(char c) {
  switch(c) {
    case '=':  return -2; break;
    case '-':  return -1; break;
    case '1':  return  1; break;
    case '2':  return  2; break;
    default:   return  0; break;
  }
}

char snafu_map(int d) {
  switch(d) {
    case -2:  return '='; break;
    case -1:  return '-'; break;
    case  1:  return '1'; break;
    case  2:  return '2'; break;
    default:  return '0'; break;
  }
}

int main() {
  FILE *fh = fopen("sample25", "r");
  //FILE *fh = fopen("input25", "r");

  char *line;
  size_t len;
  int i;
  uint64_t sum = 0;
  int8_t *digs;
  while( getline(&line, &len, fh) != -1 ) {
    for(i = 0; i < len; ++i) {
      if (line[i] == '\n')  { line[i] = '\0'; break; }
    }
    for(int d=i-1, i=0; d >= 0; --d, ++i) {
      sum += (uint64_t)pow(5, i) * digit_map(line[d]);
    }
  }

  fclose(fh);

  printf("(%s)  sum = %lld\n", line, sum);

  int8_t pad = 2*i;
  printf("pad = %d\n", pad);
  digs = (int8_t *)malloc(pad * sizeof(int8_t));
  memset(digs, 0, pad);

  free(digs);

  printf("Part A: %lld\n", 0);
  printf("Part B: %lld\n", 0);
}
