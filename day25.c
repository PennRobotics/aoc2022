#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <tgmath.h>

#define  MINBUFFERSZ  120

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

struct divmod_s {
  int64_t quot;
  uint64_t rem;
};

struct divmod_s divmod(int64_t num, uint64_t den) {
  struct divmod_s result;

  if (num < 0) {
    result.quot = (num-(den-1)) / den;
    result.rem = (num-(den-1)) % den + den - 1;
  } else {
    result.quot = num / den;
    result.rem = num % den;
  }

  return result;
}

int main() {
  char *line = (char *)malloc(MINBUFFERSZ * sizeof(char));
  size_t len;
  //FILE *fh = fopen("sample25", "r");
  FILE *fh = fopen("input25", "r");
  int i;
  uint64_t sum = 0;

  while( getline(&line, &len, fh) != -1 ) {
    for(i = 0; i < len; ++i) {
      if (line[i] == '\n')  { line[i] = '\0'; break; }
    }
    for(int d=i-1, i=0; d >= 0; --d, ++i) {
      sum += (uint64_t)pow(5, i) * digit_map(line[d]);
    }
  }

  fclose(fh);

  int8_t *digs;
  int8_t pad = 2*i;
  struct divmod_s dm;
  int8_t dig;

  digs = (int8_t *)malloc(pad * sizeof(int8_t));
  memset(digs, 0, pad);

  i = 0;
  for(;;) {
    if (sum / (uint64_t)powl(5, ++i) == 0)  { break; }
  }

  for(int d=i-1; d >= 0; --d) {
    dm = divmod(sum, (uint64_t)pow(5, d));
    dig = dm.quot;
    sum = dm.rem;
    digs[d] += dig;
    for (int scan=d; scan<i; ++scan) {
      if (digs[scan] > 2) {
        digs[scan] -= 5;
        digs[scan+1] += 1;
      }
    }
  }

  printf("Part A: ");
  for(i=pad-1; i >= 0; --i) {
    if (digs[i] != 0)  { break; }
  }
  for(int d=i; d >= 0; --d) {
    printf("%c", snafu_map(digs[d]));
  }
  printf("\n");

  free(digs);

  printf("Part B: %lld\n", 0);
}
